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

    def calcular_total(self) -> float:
        total = 0.0
        for item in self.itens:
            total += item.subtotal()
        return total

    def validar_cartao(self, numero: str, cvv: str) -> bool:
        if len(numero) != 16 or not numero.isdigit():
            return False
        if len(cvv) != 3 or not cvv.isdigit():
            return False
        return True

    def calcular_frete(self, cep: str) -> float:
        if cep.startswith("59"):
            return 12.0
        if cep.startswith("5"):
            return 25.0
        return 40.0

    def imprimir_cupom_fiscal(self) -> str:
        linhas = ["======= CUPOM FISCAL =======", f"Cliente: {self.cliente}"]
        for item in self.itens:
            linhas.append(f"{item.produto.nome:<15} x{item.quantidade}  R$ {item.subtotal():.2f}")
        linhas.append(f"TOTAL: R$ {self.calcular_total():.2f}")
        return "\n".join(linhas)


if __name__ == "__main__":
    carrinho = Carrinho("Carlos")
    carrinho.adicionar_item(Produto("Teclado", 120.0), 1)
    carrinho.adicionar_item(Produto("Mouse", 50.0), 2)
    carrinho.adicionar_item(Produto("Cabo USB", 15.0), 1)
    carrinho.remover_item("Cabo USB")
    print("Itens no carrinho:", carrinho.quantidade_de_itens())

    if carrinho.validar_cartao("1234567812345678", "123"):
        frete = carrinho.calcular_frete("59000-000")
        print(f"Frete: R$ {frete:.2f}")
        print(carrinho.imprimir_cupom_fiscal())
    else:
        print("Cartao recusado")
