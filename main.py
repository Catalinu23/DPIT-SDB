from repository.repository import Repository
from service.product_service import ProductService
from ui.console import ConsoleUI


product_repository = Repository()
product_service = ProductService(product_repository)

ui = ConsoleUI(product_service)

ui.run()
