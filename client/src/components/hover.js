import React from "react";
import { MDBContainer } from "mdb-react-ui-kit";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";

const Hover = () =>{
    return(
        <Navbar className='bg-navbar' variant='dark'>
          <MDBContainer>
            <Navbar.Brand href="/home">SPBE</Navbar.Brand>
            <Nav className="me-auto">
              <Nav.Link href="/login">Login</Nav.Link>
              <Nav.Link href="/signup">Signup</Nav.Link>
            </Nav>
          </MDBContainer>
        </Navbar>
    )
}

export default Hover ;