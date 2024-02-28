import { Component } from '@angular/core';

import { products } from '../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  products = [...products];

  share() {
    window.alert('The product has been shared!');
  }

  shareProductTg(product: any){
    const shareUrl = `https://t.me/share/url?url=${encodeURIComponent(product.link)}`;
    window.open(shareUrl, '_blank');
  }

  shareProductWs(product: any){
    const shareUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(product.link)}`;
    window.open(shareUrl, '_blank');
  }

  redirectKaspi(product:any) {
    window.open(product.link, '_blank')
  }
  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }
}


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/