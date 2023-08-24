import React from "react";

const Table = ({data}) => {

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
            <td><a className="link-secondary" href={item.url} target="_blank">{item.url.slice(0,25)}...</a></td>
            <td>{item.type}</td>
            <td>{item.topic.split(" ").map((topic) => (
              <span className="badge badge-dark">{topic}</span>
              ))}</td>
            <td><span className="badge badge-dark">{item.author}</span></td>
          </tr>
        ))}
      </tbody>
  </table>
  );
};
  
export default Table;

