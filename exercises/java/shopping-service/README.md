# Shopping Service

A Grails e-commerce application demonstrating REST API patterns, originally presented at SpringOne2GX 2014.

## Technology Stack

| Component | Version |
|-----------|---------|
| Framework | Grails 2.4.3 |
| Language | Groovy |
| Build | Gradle |
| Database | H2 (embedded) |
| ORM | Hibernate 4 + EhCache |
| Server | Tomcat 7 |
| Java | 1.6+ |

## Domain Model

The application manages four core entities:

- **Product** - Items for sale (`name`, `price`)
- **Customer** - Users who place orders (`name`, has many orders)
- **Order** - Customer orders with computed total price (`number`, `dateCreated`)
- **OrderLine** - Line items linking products to orders (`product`, `quantity`)

## REST API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/products` | List all products |
| GET | `/products/{id}` | Get product by ID |
| POST | `/products` | Create product |
| PUT | `/products/{id}` | Update product |
| DELETE | `/products/{id}` | Delete product |
| GET | `/customers` | List all customers |
| GET | `/customers/{id}` | Get customer by ID |
| GET | `/customers/{id}/orders` | Get orders for customer |
| GET | `/orders` | List all orders |
| GET | `/orders/{id}` | Get order by ID |
| POST | `/orders` | Create order |
| PUT | `/orders/{id}` | Update order |
| DELETE | `/orders/{id}` | Delete order |

Supports JSON and XML content negotiation via `Accept` header or `.json`/`.xml` extensions.

## Running the Application

```bash
# Run in development mode
./grailsw run-app

# Run tests
./grailsw test-app

# Package as WAR
./grailsw war
```

The application starts at `http://localhost:8080/shopping`

## Project Structure

```
grails-app/
├── conf/           # Configuration (DataSource, UrlMappings, Bootstrap)
├── controllers/    # REST/MVC controllers
├── domain/         # GORM domain classes
└── views/          # GSP templates
src/groovy/         # Custom renderers, REST client demos
test/unit/          # Spock unit tests
```

## Key Features Demonstrated

- **@Resource annotation** - Automatic REST endpoint generation
- **UrlMappings** - RESTful and nested resource routing (`/customers/{id}/orders`)
- **Content negotiation** - JSON, XML, and HAL format support
- **GORM relationships** - One-to-many with cascading operations
- **Computed properties** - Order price calculated from order lines
- **Scaffolding** - Automatic CRUD UI generation
- **Transactional controllers** - Read-only by default, explicit write transactions

## Architecture Diagrams

See `architecture-diagrams.html` for visual documentation of:
- High-level layered architecture
- Domain model relationships
- REST API request flow
- Component interactions

## Testing

Unit tests use Spock framework. Current coverage includes:
- Domain validation constraints
- Price calculation logic
- Controller JSON rendering

Run tests with: `./grailsw test-app`

## Known Issues

- HAL renderers on domain objects (vs collections) can be flaky
- Legacy project targeting Java 1.6 compatibility

## Author

Ken Kousen
ken.kousen@kousenit.com

---

*Originally demonstrated at SpringOne2GX 2014*
