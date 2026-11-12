from typing import List


class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome: str = nome
        self.preco: float = preco


class ItemCarrinho:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.produto: Produto = produto
        self.quantidade: int = quantidade

    def subtotal(self) -> float:
        return self.produto.preco * self.quantidade


class Carrinho:
    def __init__(self, cliente: str) -> None:
        self.cliente: str = cliente
        self.itens: List[ItemCarrinho] = []  # composição: Carrinho ◆ ItemCarrinho (0..*)

    def adicionar_item(self, produto: Produto, quantidade: int) -> None:
        if quantidade <= 0:
            raise ValueError("Quantidade invalida")
        self.itens.append(ItemCarrinho(produto, quantidade))

    def remover_item(self, nome_produto: str) -> None:
        for item in self.itens:
            if item.produto.nome == nome_produto:
                self.itens.remove(item)
                return
        raise ValueError("Produto nao esta no carrinho")

    def quantidade_de_itens(self) -> int:
        total = 0
        for item in self.itens:
            total += item.quantidade
        return total

class CalcularVendas:
    def calcular_total(self, itens: list[ItemCarrinho]) -> float:
        total = 0.0
        for item in itens:
            total += item.subtotal()
        return total

    def calcular_frete(self, cep: str) -> float:
            if cep.startswith("59"):
                return 12.0
            if cep.startswith("5"):
                return 25.0
            return 40.0

class ValidarVendas:
    # Classe ValidarVendas
    def validar_cartao(self, numero: str, cvv: str) -> bool:
        if len(numero) != 16 or not numero.isdigit():
            return False
        if len(cvv) != 3 or not cvv.isdigit():
            return False
        return True

class ImprimirCumpom:
    def __init__(self, carrinho: Carrinho):
        self.carrinho = carrinho
        
        
    # imprimircumpom
    def imprimir_cupom_fiscal(self, total: float) -> str:
        linhas = ["======= CUPOM FISCAL =======", f"Cliente: {self.carrinho.cliente}"]
        for item in self.carrinho.itens:
            linhas.append(f"{item.produto.nome:<15} x{item.quantidade}  R$ {item.subtotal():.2f}")
        linhas.append(f"TOTAL: R$ {total:.2f}")
        return "\n".join(linhas)


if __name__ == "__main__":
    carrinho = Carrinho("Carlos")
    validar = ValidarVendas() 
    calcular = CalcularVendas()
    imprimir = ImprimirCumpom(carrinho)
    carrinho.adicionar_item(Produto("Teclado", 120.0), 1)
    carrinho.adicionar_item(Produto("Mouse", 50.0), 2)
    carrinho.adicionar_item(Produto("Cabo USB", 15.0), 1)
    carrinho.remover_item("Cabo USB")
    print("Itens no carrinho:", carrinho.quantidade_de_itens())

    if validar.validar_cartao("1234567812345678", "123"):
        frete = calcular.calcular_frete("59000-000")
        print(f"Frete: R$ {frete:.2f}")
        calcular_total = calcular.calcular_total(carrinho.itens)
        print(imprimir.imprimir_cupom_fiscal(calcular_total))
    else:
        print("Cartao recusado")
