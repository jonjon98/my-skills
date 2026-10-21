# Spring Boot rules

These extend `../SKILL.md` and `../java/RULES.md`. Apply the Java rules to all Spring Boot code.

## Layers

- Keep controllers thin. A controller reads the request, calls one service method, and returns the response. It holds no business logic.
- Put business rules in service classes. A service method is the unit of a transaction.
- Put data access in repositories. Do not query the database from controllers or services with raw SQL scattered through them.
- Do not return JPA entities from controllers. Map them to response records first, so the API contract does not change when the table does.

## Injection and configuration

- Inject dependencies through the constructor, with `final` fields. Do not use field injection with `@Autowired` on fields. Constructor injection makes each dependency visible and the class testable without Spring.
- Bind configuration to a `@ConfigurationProperties` record. Do not scatter `@Value` strings across the code.
- Read secrets from the environment or a secret store, never from a committed properties file.

## Requests and errors

- Validate request bodies with `@Valid` on a request record that carries constraint annotations.
- Handle errors in one `@RestControllerAdvice` class that maps each named exception to a status code. Do not catch exceptions inside each controller method.
- Name each exception for the failure, such as `InvoiceNotFoundException`.

## Transactions

- Put `@Transactional` on service methods, not on controllers or repositories.
- Keep each transactional method to one unit of work. Call other services from it only when they belong to the same unit.

## Logging

- Log through SLF4J with placeholders, such as `log.info("Invoice {} paid", invoiceId)`. Do not concatenate strings in log calls.
- Log an error once, where it is handled. Do not log and rethrow the same exception.
