const fetchProdutos = () => {
    const url = `http://localhost:8000/produto/`;

    fetch(url)
        .then(response => response.json())
        .then(produtos => {
            console.log(produtos);
        });
}

fetchProdutos();