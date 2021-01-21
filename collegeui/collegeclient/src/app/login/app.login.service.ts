import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http'
interface LoginDetials{
    responseData : {"token":String, "status":Number},
    status : String;
}
@Injectable({providedIn : 'root'})
export class LoginService {

    constructor(private http : HttpClient){}
    httpHeaders = new HttpHeaders({'Content-type': 'application/json'})
    Login(email:String, password:String):Observable<LoginDetials>{
        
        return this.http.post<LoginDetials>('http://localhost:8000/adminlogin/',{
            username:email,
            password: password
        })
    }
}