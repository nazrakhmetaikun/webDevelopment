import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
import {Album, Photos} from './models';




@Injectable({
  providedIn: 'root'
})
export class AlbumsService {
  BASE_URL = 'https://jsonplaceholder.typicode.com';


  constructor(private client:HttpClient) { }
  getAlbums(): Observable<Album[]> {
    return this.client.get<Album[]>(`${this.BASE_URL}/albums`);
  }

  getAlbum(id: number): Observable<Album> {
    return this.client.get<Album>(`${this.BASE_URL}/albums/${id}`);
  }
  deleteAlbum(id: number): Observable<any> {
    return this.client.delete(`${this.BASE_URL}/albums/${id}`);
  }
  updateAlbum(album: Album): Observable<Album>{
    return this.client.put<Album>(`${this.BASE_URL}/albums/${album.id}`, album);
  }
  addAlbum(album: Album): Observable<Album> {
    // @ts-ignore
    return this.client.post(`${this.BASE_URL}/albums`, album);
  }
  getAlbumPhotos(id: number): Observable<Photos[]>{
    // @ts-ignore
    return this.client.get(`${this.BASE_URL}/albums/${id}/photos`);

  }
}