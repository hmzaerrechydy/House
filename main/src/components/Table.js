import React from "react";

const Table = ({data}) => {

  const url = (u) => {
    if(u.length <= 25){
      return u; 
    }else{
      return u.slice(0,25) + '...'; 
    }
  }
  
  return (
    <table className="table table-hover">
        <thead>
        <tr className="table-light">
          <th>Title</th>
          <th>URL</th>
          <th>Type</th>
          <th>Topic</th>
          <th>Author</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item) => (
          <tr key={item.id}>
            <td>{item.title}</td>
            <td><a className="link-secondary" href={item.url} target="_blank">{url(item.url)}</a></td>
            <td>{item.type}</td>
            <td>{item.topic}</td>
            <td>{item.author}</td>
          </tr>
        ))}
      </tbody>
  </table>
  );
};
  
export default Table;

