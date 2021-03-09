import { Component, OnInit } from '@angular/core';
import {Album, Photos} from '../models';
import {AlbumsService} from '../albums.service';
import {ActivatedRoute} from '@angular/router';
@Component({
  selector: 'app-album-photos',
  templateUrl: './album-photos.component.html',
  styleUrls: ['./album-photos.component.css']
})
export class AlbumPhotosComponent implements OnInit {
  photos: Photos[];
  album!: Album;

  constructor(private albumsService: AlbumsService,
              private route: ActivatedRoute) {
    this.photos = [];
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get('id'));
      this.albumsService.getAlbumPhotos(id).subscribe((photos) =>{
        this.photos = photos;
      });
    });

  }



}
