from repository_layer.repository import contact_repository
from flask import request, jsonify
from flask_openapi3 import APIBlueprint,Tag
from presentation_layer.schemas import ContactSchema,ContactDelSchema, ContactViewSchema, ErrorSchema

contact_tag = Tag(name="Contatos", description="Operações relacionadas a contatos")
contact_bp = APIBlueprint('contact_bp', __name__, abp_tags=[contact_tag])

@contact_bp.get('/contacts/', tags=[contact_tag])
def get_contacts():
    try:
        contacts = contact_repository.list_contacts()
        return jsonify(contacts), 200
    except Exception:
        return jsonify({"erro": "Não foram encontrados dados."}), 400


@contact_bp.put('/contact/', tags=[contact_tag],
                responses={
                    "200": ContactViewSchema,
                    "400": ErrorSchema,
                    "404": ErrorSchema
                })
def atualizar_contato(body:ContactViewSchema):
    """
    Atualiza um contato
    """

    contato = contact_repository.update_contact(body.contact_id, body.name, body.phone, body.address)
    if not contato:
        return jsonify({"erro": "Contato não encontrado."}), 404

    return jsonify(contato), 200


@contact_bp.delete('/contact/', tags=[contact_tag],
                    responses={
                       "200": ContactDelSchema, 
                       "404": ErrorSchema
                   })
def remover_contato(body:ContactDelSchema):
    success = contact_repository.delete_contact(body.contact_id)
    if not success:
        return jsonify({"message": "Contato não encontrado."}), 404
    return jsonify({"contact_id": body.contact_id}), 200

@contact_bp.post('/contact/', tags=[contact_tag], 
                 responses={
                    "200": ContactSchema, 
                    "409": ErrorSchema, 
                    "400": ErrorSchema
                 })
def create_contact(body:ContactSchema):
    """
    Cria um novo contato.
    
    **Parâmetros da requisição:**
    - name (string): Nome do contato.
    - phone (string): Telefone do contato.
    - address (string): Endereço do contato.
    
    **Resposta:**
    - 201: Contato criado com sucesso.
    - 400: Campos obrigatórios não fornecidos ou dados inválidos.
    """
    
    contact_save = contact_repository.create_contact(
        body.name,
        body.phone,
        body.address
    )
    return contact_save, 201
