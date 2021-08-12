import React from 'react'
import { Query } from 'react-apollo'
import gql from 'graphql-tag'

const Items = () => (
    <Query query={gql`
        {
            allItems{
                name
                price
                description
                section
                restaurant{
                  id
                  name
                  address
                }
            }
        }
    `}
    >
        {({loading, error, data}) => {
            if (loading) return <p>Loading...</p>;
            if (error) return <p>Error...</p>
            return data.allItems.map(({id, name, price, section, description, restaurant }) => (
                <div key={id}>
                    <h2>{name}</h2>
                    <p>{price}</p>
                    <p>{description}</p>
                    <p>{section}</p>
                </div>
            ))
        }}
    </Query>

);

export default Items;