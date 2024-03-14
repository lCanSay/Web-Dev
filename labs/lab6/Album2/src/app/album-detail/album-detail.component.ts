import { Component } from '@angular/core';
import { Album } from '../models';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { AlbumService } from '../album.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';


@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './album-detail.component.html',
  styleUrl: './album-detail.component.css'
})
export class AlbumDetailComponent {
  album!: Album;

  constructor(private route: ActivatedRoute, private albumService: AlbumService) {
  }

  ngOnInit() {
    this.getAlbum();
  }

  getAlbum(){
    this.route.paramMap.subscribe((params) => {
      const albumId = Number(params.get('id'));
      this.albumService.getAlbum(albumId).subscribe((album) => {
        this.album = album;
      });
    });
  }

  updateAlbum() {
    this.albumService.updateAlbum(this.album).subscribe((album) => {
      this.album = album;
    });
    alert('Album updated!\n' + JSON.stringify(this.album));
  }
}