function Register(){
    return (
        <>
            <h1>Registration</h1>
            <br />
            <form>
                <label>
                    Name 
                    <input
                        type='text'
                        placeholder='Enter a Name'
                    >
                    </input>
                </label>
                <br />
                <label>
                    NickName 
                    <input
                        type='text'
                        placeholder='Enter a Nickname'
                    >
                    </input>
                </label>
                <br />
                <label>
                    Password 
                    <input
                        type='password'
                        placeholder='Enter a Password'
                    >
                    </input>
                </label>
                <br />
                <input
                    type='submit'
                >
                </input>
            </form>
        </>
    );
};

export default Register;