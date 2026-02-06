export interface Product {
  id: number;
  name: string;
  category: string;
  price: number;
  url: string;
  source: string;
  is_small_dog_friendly: boolean;
  size_recommendation: string | null;
}