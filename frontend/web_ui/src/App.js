import { BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import React, {useState, useRef} from 'react';
import Dev from './pages/dev.js';
import UI from './pages/ui.js'
import SignIn from './pages/signIn.js';
import Register from './pages/register.js';



function App() {

  const [user, setUser] = useState(null);

  return (
    <>
      <Router>
        <Routes>
          <Route path='/' exact element={<UI />} />
          <Route path='/dev' element={<Dev />} />
          <Route path='/login' element={<SignIn />}/>
          <Route path='/register' element={<Register />} />
          <Route path='*' element={<h1>ERROR</h1>} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
