import { Component } from '@angular/core';
import { categories } from '../categories';


@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrl: './category.component.css'
})
export class CategoryComponent {
  categories = [...categories]
}
