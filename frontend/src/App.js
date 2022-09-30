import React, { useEffect, useState } from 'react'
import axios from 'axios'
import './App.css'
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

const App = () => {
  const [posts, setPosts] = useState([])
  const getPosts = async () => {
    try {
      const userPosts = await axios.get("http://localhost:5004/api/v1/data")

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
    <Table striped bordered hover variant="dark">
      <TableHead>
        <TableRow>
          <TableCell >Name</TableCell >
          <TableCell >Price</TableCell >
          <TableCell >1h%</TableCell >
          <TableCell >24h%</TableCell >
          <TableCell >7d%</TableCell >
          <TableCell >Market Cap</TableCell >
          <TableCell >Volume(24h)</TableCell >
          <TableCell >Circulating Supply</TableCell >
        </TableRow>
      </TableHead>
      <tbody>

        {posts.map(post => (
          <TableRow>
            <TableCell >{post[0]}</TableCell >
            <TableCell >{post[1]}</TableCell >
            <TableCell >{post[2]}</TableCell >
            <TableCell >{post[3]}</TableCell >
            <TableCell >{post[4]}</TableCell >
            <TableCell >{post[5]}</TableCell >
            <TableCell >{post[6]}</TableCell >
            <TableCell >{post[7]}</TableCell >
          </TableRow>
        ))}
      </tbody>
    </Table>
  );
}
export default App;