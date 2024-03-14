import { Component, OnInit } from '@angular/core';
import { Photo } from '../models';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { AlbumService } from '../album.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-album-photos',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './album-photos.component.html',
  styleUrl: './album-photos.component.css'
})
export class AlbumPhotosComponent implements OnInit{
  photos!: Photo[];
  loaded: boolean = false;

  constructor(private route: ActivatedRoute, 
              private albumService: AlbumService) {
  }

  ngOnInit() {
    this.getPhotos();
  }

  getPhotos() {
    this.route.paramMap.subscribe((params) => {
      const albumId = Number(params.get('id'));
      this.loaded = false;
      this.albumService.getPhotos(albumId).subscribe((photos) => {
        this.photos = photos;
        this.loaded = true;
      });
    })
  }
}