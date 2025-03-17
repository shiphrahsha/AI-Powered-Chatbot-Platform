import { io } from 'socket.io-client';

//connecting socket to the localhost
const socket = io('http://localhost:5000');

export default socket;