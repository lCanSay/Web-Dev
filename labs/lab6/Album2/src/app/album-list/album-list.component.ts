import { Component } from '@angular/core';
import { albums } from '../albums';



@Component({
  selector: 'app-album-list',
  templateUrl: './album-list.component.html',
  styleUrl: './album-list.component.css'
})
export class AlbumListComponent {
  albums = [...albums]
}
