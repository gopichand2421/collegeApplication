import {Component } from '@angular/core';
import {NgForm} from '@angular/forms';
import {LoginService } from './app.login.service';
import {Router} from '@angular/router'


@Component({
    selector : 'app-login',
    templateUrl : './app.login.html',
    styleUrls: ['./app.login.scss']
})
export class LoginComponent{
    
    constructor(private loginservice: LoginService, private router:Router){}

    msg:String = "";
    errStatus:Boolean = false

    onSubmit(form: NgForm){
        const email = form.value.email
        const password = form.value.password
        this.loginservice.Login(email,password).subscribe(
            resData => {
                console.log(resData.status)
                if(Number(resData.status) == 200){
                    console.log("user Logged in succfully");
                    localStorage.setItem('userLoggedIn','true');
                    console.log(localStorage.getItem('userLoggedIn'))
                    this.router.navigate(['./student'])
                }else{
                }
                // console.log(Number(resData.status) == 200)
            },
            error =>{
                localStorage.setItem('userLoggedIn','false');
                if(error.status === 500){
                    this.errStatus = true
                    this.msg = 'username or password are wrong';

                }
            }
        )
        
    }

    getDisplay(){
        return this.errStatus === true ? 'block' : 'none';
    }

}