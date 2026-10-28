# Terraform rules

These extend `../SKILL.md`. The core hard rules apply in full. Terraform is declarative, so most of the clean-code rules apply to names, file layout, and how values flow between blocks.

## Baseline

- Run `terraform fmt` and `terraform validate` on every changed file. Never hand-format against them.
- Keep lines within 120 columns. Break long conditions across lines by wrapping them in parentheses.
- Pin the Terraform version and each provider version in `versions.tf`.
- Split files by job: `versions.tf`, `providers.tf`, `variables.tf`, `main.tf`, `outputs.tf`. Put a module's resources in files named for what they create, such as `network.tf` or `database.tf`, not in one large `main.tf`.
- Name each resource for its role, not its type: `aws_s3_bucket.invoice_archive`, not `aws_s3_bucket.bucket1`.
- Use snake_case for block labels, variable names, and output names.

## Explicit over compact

- Prefer concrete `object` types over free-form `map` types for variables, so each allowed field is named and typed.
- Give every variable a `description`, a `type`, and a `validation` block when a bad value would be expensive to find later:

  ```hcl
  variable "retention_days" {
    description = "How many days invoice archives are kept before deletion."
    type        = number

    validation {
      condition     = var.retention_days >= 1 && var.retention_days <= 3650
      error_message = "retention_days must be between 1 and 3650."
    }
  }
  ```

- Put every intermediate value in a named `locals` block, so each `resource` reads as a list of named inputs. Keep shared tags in one `locals` map and merge it into each resource's tags.
- Set `nullable = false` on variables that must have a value. Give object fields defaults with `optional()` instead of repeating a whole object.
- Avoid nested ternaries. Name each condition in `locals`, then use it once:

  ```hcl
  locals {
    is_production   = var.environment == "production"
    retention_days  = local.is_production ? 365 : 30
  }
  ```

- Use `count` for on/off toggles. Use `for_each` over a map or set for collections, since `count` shifts indexes and recreates later items when an earlier one is removed.
- Avoid `for` expressions that chain more than two steps. Split them into named locals.

## Phases in code

A module's `locals` should read as validate, derive, then use:

```hcl
locals {
  is_production  = var.environment == "production"
  retention_days = local.is_production ? 365 : 30
  bucket_name    = "${var.project}-${var.environment}-invoice-archive"
}

resource "aws_s3_bucket" "invoice_archive" {
  bucket = local.bucket_name
}
```

## Modules

- A module does one job and exposes only what callers need through `variables.tf` and `outputs.tf`.
- Do not reach into another module's resources. Pass its outputs in as variables.
- Keep modules shallow. Two levels of nesting is the limit.

## Secrets and state

- Never put a secret value in a `.tf` file or a `.tfvars` file that is committed. Read it from the secret store with a data source, or from an environment variable.
- Mark outputs or variables that carry secrets with `sensitive = true`.
- Do not hand-edit state. Write an explicit `moved` block to rename a resource, including when adding `count` or `for_each` to an existing one. Use `removed` blocks to drop one from state. Moved blocks need Terraform 1.1 or later.

## Comments

- Keep the core comment rules. Use `description` on variables and outputs instead of comments above them.
- A comment that explains a provider quirk, with a link to its issue, is allowed.

## Sources

- [HashiCorp Terraform style guide](https://developer.hashicorp.com/terraform/language/v1.12.x/style)
- [HashiCorp refactoring with moved blocks](https://developer.hashicorp.com/terraform/language/v1.7.x/modules/develop/refactoring)
- [Terraform skill for count, for_each, and naming](https://tessl.io/registry/skills/github/antonbabenko/terraform-skill/terraform-skill--terraform-skill)
- [Terraform skill for modern variable types](https://tessl.io/registry/skills/github/bkircher/skills/terraform)
