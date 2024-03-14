import { Component, OnInit } from '@angular/core';
import { Album } from '../models';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { AlbumService } from '../album.service';
import { FormsModule } from '@angular/forms';



@Component({
  selector: 'app-album-list',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './album-list.component.html',
  styleUrl: './album-list.component.css'
})
export class AlbumListComponent implements OnInit{
  albums! : Album[];
  altAlbums: Album[] | undefined;

  constructor(private albumService: AlbumService) {}

  ngOnInit() {
    this.getAlbums(); 
  }

  getAlbums() {
    //this.loaded = false;
    this.albumService.getAlbums().subscribe((albums) => {
      this.albums = albums;
      //this.loaded = true;
    });
  }

  deleteAlbum(id: number) {
    this.albums = this.albums.filter(album => album.id !== id);
    this.albumService.deleteAlbum(id).subscribe();
  }
}


