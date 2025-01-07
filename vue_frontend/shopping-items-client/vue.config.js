module.exports = {
  devServer: {
    https: true, // Enable HTTPS
    host: '0.0.0.0', // Optional: Expose dev server to other devices in your network
    port: 8082, // Optional: Set the port
    client: {
      webSocketURL: {
        protocol: 'wss',
        hostname: 'musical-palm-tree-55pgqgxwqx295.github.dev', // Use your server hostname here
        port: 8082,
      },
    },
  },
};
