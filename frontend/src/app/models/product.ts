export class Product{
    productId: number;
    productName: string;
    productStock: number; 
    productDescription: string;
    productImage: string;
    price: number;
    reviewID: number[];

    constructor(productId: number, productName: string, productStock: number, productDescription: string, productImage: string, price: number, reviewID: number[]){
      this.productId = productId;
      this.productName = productName;
      this.productStock = productStock;
      this.productDescription = productDescription;
      this.productImage = productImage;
      this.price = price;
      this.reviewID = reviewID;
    }
}