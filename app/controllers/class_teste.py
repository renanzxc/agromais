class Perfil(object):
	def __init__(self,nome,sobrenome,email,senha,cpf):
		self.nome = nome
		self.sobrenome = sobrenome
		self.email = email
		self.senha = senha
		self.cpf = cpf
	
	def getNome(self):
		return self.nome

	def getSobrenome(self):
		return self.sobrenome

	def getEmail(self):
		return self.email

	def getSenha(self):
		return self.senha

	def getCpf(self):
		return self.cpf

class PerfilComprador(Perfil):
	def __init__(self,nome,sobrenome,contato,cidade,bairro,endereco,cpf,email,senha):
		super().__init__(nome,sobrenome,email,senha,cpf)
		self.contato = contato
		self.cidade = cidade
		self.bairro = bairro
		self.endereco = endereco		

	#GETS
	
	def getContato(self):
		return self.contato

	def getCidade(self):
		return self.cidade

	def getBairro(self):
		return self.bairro

	def getEndereco(self):
		return self.endereco


class PerfilProdutor(PerfilComprador):

	def __init__(self,nome,sobrenome,contato,cidade,bairro,endereco,cpf,email,senha,nome_loja,contato_comercial,endereco_comercial,descricao_loja,foto_loja):
		super().__init__(nome,sobrenome,contato,cidade,bairro,endereco,cpf,email,senha)
		self.nome_loja = nome_loja
		self.contato_comercial = contato_comercial
		self.endereco_comercial = endereco_comercial
		self.descricao_loja = descricao_loja
		self.foto_loja = foto_loja

	def getNome_loja(self):
		return self.nome_loja

	def getDescricao_loja(self):
		return self.descricao_loja

	def getContato_comercial(self):
		return self.contato_comercial

	def getEndereco_comercial(self):
		return self.endereco_comercial

	def getFoto(self):
		return self.foto_loja


class Login():
	def __init__(self,email,senha):
		self.email = email
		self.senha = senha

	def getEmail(self):
		return self.email

	def getSenha(self):
		return self.senha

class Produto():
	def __init__(self,nome_produto,categoria,subcategoria,preco,estoque,descricao_produto,id_produtor):
		self.nome_produto = nome_produto
		self.categoria = categoria
		self.subcategoria = subcategoria
		self.preco = preco
		self.estoque = estoque
		#self.foto_produto = foto_produto
		self.descricao_produto = descricao_produto
		self.id_produtor = id_produtor

	def getNome_produto(self):
		return self.nome_produto

	def getCategoria(self):
		return self.categoria

	def getSubcategoria(self):
		return self.subcategoria

	def getPreco(self):
		return self.preco

	def getEstoque(self):
		return self.estoque

	def getDescricao_produto(self):
		return self.descricao_produto

	def getId_produtor(self):
		return self.id_produtor