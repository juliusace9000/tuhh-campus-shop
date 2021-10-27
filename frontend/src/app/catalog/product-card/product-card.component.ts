import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-product-card',
  templateUrl: './product-card.component.html',
  styleUrls: ['./product-card.component.css']
})


export class ProductCardComponent implements OnInit {

  products = [{
    productId: 1, 
    productName: "Faber-Castell Jumbo Grip Silber",
    productStock: 3, 
    productDescription: "This is the best pencil ever. Grip wunderful. Much Wow. Such amazing", 
    productImage: "../assets/images/pencil.png",
    price: 2.99,
    reviewID: [] 
  
  }]

  constructor() { }

  ngOnInit(): void {
  }

}
