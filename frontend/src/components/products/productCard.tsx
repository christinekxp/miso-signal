import type { Product } from "../../types/product";

interface Props {
  product: Product;
}

function ProductCard({ product }: Props) {
  return (
    <div style={{ border: "1px solid #ddd", padding: "1rem", marginBottom: "1rem" }}>
      <h3>{product.name}</h3>
      <p>${product.price}</p>
      <p>{product.source}</p>

      <a href={product.url} target="_blank" rel="noopener noreferrer">
        View product
      </a>
    </div>
  );
}

export default ProductCard;
