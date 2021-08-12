import './App.css';
import ApolloClient from 'apollo-boost';
import {ApolloProvider} from 'react-apollo'
import Restaurants from './Restaurants'
import Items from './Items';


const client = new ApolloClient({
  uri: "http://127.0.0.1:8000/graphql"
});

const App = () => (
  <ApolloProvider client={client}>
    <div className="section">
      <h1 className="main-header">What's Good</h1>
      <div className="flex-wrapper">
        <h2 className="list-header">list all restaurants</h2>
        <div className="flex">
          <Restaurants />
        </div>
        <h2 className="list-header">list all Menu Items</h2>
        <div className="flex">
        <Items />
        </div>
      </div>
    </div>
  </ApolloProvider>
)

export default App;
