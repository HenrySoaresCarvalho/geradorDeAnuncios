def template(carro,listaCarros,sku,pos,comp,larg,alt):
        temp = f""" 
        TITULO: Pastilha De Freio {pos} em Nanocerâmica {carro}
    DESCRIÇÃO: Jogo de Pastilhas {pos} em Excelente qualidade!!!

    A Blue Friction® é uma industria especializada em freios de veículos leves, médios e pesados. 
    Somando as suas plantas fabris pelo mundo, são produzidos cerca de 10 de milhões de peças por ano, 
    que atendem as especificações das maiores e melhores montadoras do planeta.

    A Blue Friction desenvolveu em seus laboratórios um composto exclusivo chamado de nanoceramic,  
    cuja principal função é obter por meio de nano partículas de cerâmica, uma mistura mais homogenia  
    entre o composto cerâmico e demais componentes da massa de atrito em que proporciona um aumento considerável  
    do coeficiente de fricção dos produtos Blue Friction.

    Cansado de chiadeira nas rodas em seu veículo?
    Blue Friction é a solução!!
    100% dos Clientes APROVAM pastilhas de freio Blue Friction!!

    Compatível com:
    {listaCarros}

    Para demais aplicações, informe o chassi nas perguntas para confirmarmos!!

    Especificação Técnica:
    • Código Blue Friction®: {sku}
    • Pastilhas em nanocerâmica
    • Aplicação: {pos.title()}
    • Material de atrito chanfrado para menor ruído
    • Manta com baixo nível de ruído (tecnologia Blue Performance)
    • Melhor Dissipação de Calor e Atrito com o Disco de Freio
    • Não Libera Gases Tóxicos
    • Dimensões Aproximadas (CxLxE): [{comp}, {larg}, {alt}]
    • Certificações: INMETRO, ISO14001, ECE-R90, ISO/TS16949, OHSAS18001

    Conteúdo da Embalagem:
    • 04 Pastilhas de Freio em nanocerâmica

    Importante:
    Garantia de 90 dias.

    Recomendamos que a instalação seja feita por profissional especializado e não nos responsabilizamos pelo mau uso do produto.
            """
        return temp        