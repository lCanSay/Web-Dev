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
  newAlbumTitle: string = '';
  albums! : Album[];
  altAlbums: Album[] | undefined;

  constructor(private albumService: AlbumService) {}

  ngOnInit() {
    this.getAlbums(); 
  }

  getAlbums() {
    this.albumService.getAlbums().subscribe((albums) => {
      this.albums = albums;
    });
  }

  createAlbum() {
    const newAlbum: Album = { id: this.albums.length + 1, title: this.newAlbumTitle };
    this.albums.push(newAlbum);
    this.newAlbumTitle = '';
  }

  deleteAlbum(id: number) {
    this.albums = this.albums.filter(album => album.id !== id);
    this.albumService.deleteAlbum(id).subscribe();
  }
}


