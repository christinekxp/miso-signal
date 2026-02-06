import ProductList from "../components/products/productList";

function HomePage() {
  return (
    <main style={{ padding: "2rem" }}>
      <h1>Miso’s Picks 🐶</h1>
      <p>Products curated for small dogs.</p>

      <ProductList />
    </main>
  );
}

export default HomePage;
