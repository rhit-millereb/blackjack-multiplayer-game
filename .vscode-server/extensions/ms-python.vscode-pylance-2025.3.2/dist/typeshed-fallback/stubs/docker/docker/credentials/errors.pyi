from subprocess import CalledProcessError

class StoreError(RuntimeError): ...
class CredentialsNotFound(StoreError): ...
class InitializationError(StoreError): ...

def process_store_error(cpe: CalledProcessError, program: str) -> Exception: ...
