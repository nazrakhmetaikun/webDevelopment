import { Component, OnInit } from '@angular/core';
import { Album } from '../models';
import {ActivatedRoute} from '@angular/router';
import { ALBUMS } from '../albums-db';
import {Location} from '@angular/common';
import { AlbumsService } from '../albums.service';


@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
  export class AlbumDetailComponent implements OnInit {
    album!: Album;
    loaded!: boolean | undefined;
  
    constructor(private route: ActivatedRoute,
                private location: Location,
                private albumsService: AlbumsService) {  }
  
    ngOnInit(): void {
      this.getPost();
    }
  
    getPost() {
      this.route.paramMap.subscribe((params) => {
        const id = Number(params.get('id'));
        this.loaded = false;
        this.albumsService.getAlbum(id).subscribe((album) => {
          this.album = album;
          this.loaded = true;
        });
      });
    }
  
    updateAlbum() {
      this.albumsService.updateAlbum(this.album).subscribe((album) => {
        console.log(album);
      });
    }
  
    goBack() {
      this.location.back();
    }
  
  }
