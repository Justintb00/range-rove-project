import React, {useState} from 'react';
import { Navigate, Link} from 'react-router-dom';

function SignIn(){
    const [loggedIn, setLoggedIn] = useState(null);

    function checkSignIn(){
        if (loggedIn){
            <Navigate to='/' />
        }
        
    };
    
    return(
        <>
            <form>
                <label>
                    Username: 
                    <input
                        type="text"
                    >

                    </input>
                </label>
                <br />
                <label>
                    Password: 
                    <input
                        type="text"
                    >
                    </input>
                </label>
                <br />
                <button
                    type="submit"
                >
                    Sign In
                </button>
            </form>
            <br />
            <Link to='/register'>Register</Link>
        </>
    );
}

export default SignIn;