# Shopping Service - Claude Code Context

This file provides context for AI assistants working with this codebase.

## Project Overview

A legacy Grails 2.4.3 e-commerce application demonstrating REST API patterns. Originally a demo from SpringOne2GX 2014, now used as a training exercise for modernization and refactoring.

## Technology Stack

- **Framework**: Grails 2.4.3 (Groovy-based, Spring-backed)
- **Build**: Gradle with Grails plugin
- **Database**: H2 embedded (development), configurable for production
- **ORM**: GORM (Grails Object Relational Mapping) over Hibernate 4
- **Testing**: Spock framework
- **Java Compatibility**: 1.6+

## Key Files and Locations

### Domain Classes (`grails-app/domain/s2gx/`)
- `Product.groovy` - Items for sale (name, price)
- `Customer.groovy` - Users with orders relationship
- `Order.groovy` - Orders with computed price, belongs to Customer
- `OrderLine.groovy` - Line items linking Order to Product

### Controllers (`grails-app/controllers/s2gx/`)
- `ProductController.groovy` - Scaffolded + custom JSON actions
- `CustomerController.groovy` - Scaffolded + custom JSON actions
- `OrderController.groovy` - Full REST implementation with transactions
- `OrderLineController.groovy` - Basic scaffolded controller

### Configuration (`grails-app/conf/`)
- `UrlMappings.groovy` - REST resource mappings including nested routes
- `DataSource.groovy` - Database configuration per environment
- `BootStrap.groovy` - Sample data initialization
- `Config.groovy` - Application configuration

### Tests (`test/unit/s2gx/`)
- Domain specs test validation constraints
- Controller specs test REST endpoints
- **Note**: CustomerControllerSpec and OrderLineControllerSpec are empty placeholders

## Common Tasks

### Running the Application
```bash
./grailsw run-app
# Starts at http://localhost:8080/shopping
```

### Running Tests
```bash
./grailsw test-app
```

### Building
```bash
./grailsw war
```

## Architecture Patterns

### REST Endpoints
- Uses `@Resource` annotation for automatic REST generation
- Manual controller actions for custom JSON rendering
- Nested URL mappings: `/customers/{id}/orders`
- Content negotiation: JSON, XML via Accept header or file extension

### Domain Relationships
```
Customer (1) ──────< Order (many)
Order (1) ──────< OrderLine (many)
OrderLine >────── Product (1)
```

### Transaction Management
- Controllers use `@Transactional(readOnly = true)` at class level
- Write operations (`save`, `update`, `delete`) have explicit `@Transactional`

## Known Issues and Technical Debt

1. **Empty test files**: CustomerControllerSpec and OrderLineControllerSpec need implementation
2. **Incomplete test setup**: OrderControllerSpec has TODO for `populateValidParams`
3. **Debug code**: ProductControllerSpec contains `println` statements
4. **Edge cases untested**: Empty orderLines, null product in OrderLine
5. **No service layer**: Business logic in controllers and domain classes
6. **Legacy Java target**: Still targeting Java 1.6

## Refactoring Opportunities

- Extract service layer for business logic
- Modernize to Grails 4.x+ or migrate to Spring Boot
- Add comprehensive integration tests for REST API
- Implement proper error handling and validation responses
- Add pagination support to list endpoints

## Code Style

- Groovy conventions with dynamic typing
- Spock BDD-style test specifications
- GORM static blocks for constraints and mappings

## Related Documentation

- `architecture-diagrams.html` - Visual architecture documentation with Mermaid diagrams
- `README.md` - User-facing project documentation
