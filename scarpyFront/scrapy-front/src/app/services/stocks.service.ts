import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
@Injectable({
  providedIn: 'root'
})
export class StocksService {
  private   apiUrl = environment.apiurl;

private  httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};
  constructor(private http: HttpClient) {}

  getData(): Observable<any> {
    console.log('URL de la Solicitud:', this.apiUrl);

    return this.http.get<any>(this.apiUrl);
  }

  //: Observable<any>
  cargarAssets(data,id):Observable<any> {
    let newurl=this.apiUrl +"/saveAssets.php"
    let postData = { key: id,
                      data:data
    };
    console.log(postData)
   return this.http.post<any>(newurl, postData,this.httpOptions)

  }
  getUserAssets(key){
    let newurl=this.apiUrl +"/getUserAssets.php?key=" +key
    return this.http.get<any>(newurl);

  }
}
