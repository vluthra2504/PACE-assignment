import React, { useEffect, useState } from 'react'
import axios from 'axios'
import './App.css'
import Table from 'react-bootstrap/Table';

const App = () => {
  const [posts, setPosts] = useState([])
  const getPosts = async () => {
    try {
      const userPosts = await axios.get("http://localhost:5000/api/v1/data")

      setPosts(userPosts.data);  // set State

    } catch (err) {
      console.error(err.message);
    }
  };

  useEffect(() => {

    getPosts()
    const interval = setInterval(() => {
      getPosts()
    }, 3000)


    return () => clearInterval(interval)
  }, [])  // includes empty dependency array
  return (
    // <div>
    //   <h1>useEffect</h1>
    <Table striped bordered hover>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
          <th>1h%</th>
          <th>24h%</th>
          <th>7d%</th>
          <th>Market Cap</th>
          <th>Volume(24h)</th>
          <th>Circulating Supply</th>
        </tr>
      </thead>
      <tbody>

        {posts.map(post => (
          <tr>
            <td>{post[0]}</td>
            <td>{post[1]}</td>
            <td>{post[2]}</td>
            <td>{post[3]}</td>
            <td>{post[4]}</td>
            <td>{post[5]}</td>
            <td>{post[6]}</td>
            <td>{post[7]}</td>
          </tr>
        ))}
      </tbody>
    </Table>
  );
}
export default App;