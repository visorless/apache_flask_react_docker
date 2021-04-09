import React, {useEffect, useState} from 'react'
import axios from 'axios'
import './App.css';

function App() {
    const [data, setData] = useState(0)

    useEffect( () => {
        axios.get('/api/data')
        .then( response => {
            setData(response.data)
        })
    }, [])

    return (
    <div className="App">
        <h1>Hello World!</h1>
        <h2>{data}</h2>
    </div>
  );
}

export default App;
