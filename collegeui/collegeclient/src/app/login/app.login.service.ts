import {Injectable} from '@angular/core';
import {Observable, throwError} from 'rxjs';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import {catchError} from 'rxjs/operators';
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
        .pipe(catchError(this.handleError))
    }

    private handleError(errorRes : HttpErrorResponse){
        let errorMessage = 'An unknow error message occured';

        if(!errorRes.error || !errorRes.error.error){
            return throwError(errorMessage);
        }
        switch(errorRes.error.error.message){

        }
        return throwError(errorMessage);
    }
}