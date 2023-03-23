import React from "react";
import Signupcard from "./signup";
import Camera from "./webcamsgn";
import Hover from './hover';
import './signup.css'

const Signup=()=>{
    
    return(
        <div className="background">
            <div className="hover">
                <Hover/>
            </div>
            <div className="camera">
                <Camera/>
            </div>
            <div className="card">
                <Signupcard/>
            </div>
        </div>
    )    
}

export default Signup;