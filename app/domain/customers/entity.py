class Customer:
    def __init__(
        self,
        identification: str,
        dv: str,
        names: str,
        address: str,
        email: str,
        phone: str,
        legal_organization_id: str,
        tribute_id: str,
        identification_document_id: str,
        municipality_id: str,
        company: str = "",
        trade_name: str = "",
        id: int | None = None,
    ):
        self.id = id
        self.identification = identification
        self.dv = dv
        self.company = company
        self.trade_name = trade_name
        self.names = names
        self.address = address
        self.email = email
        self.phone = phone
        self.legal_organization_id = legal_organization_id
        self.tribute_id = tribute_id
        self.identification_document_id = identification_document_id
        self.municipality_id = municipality_id
