import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs'
import { LoginService } from '../login/app.login.service';

@Component({
    selector:'app-home',
    templateUrl : './app.home.component.html',
    styleUrls : ['./app.home.component.scss',]
})
export class AppHomeComponent implements OnInit,OnDestroy{
    
    constructor(private loginservice : LoginService){

    }

    ngOnInit(){
        // this.loginservice.
    }

    ngOnDestroy(){
        
    }
}