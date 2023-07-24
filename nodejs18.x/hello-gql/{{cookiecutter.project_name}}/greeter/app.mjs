export const lambdaHandler = async (event, _) => {
  console.log("Got an Invoke Request.");
  console.log(`EVENT: ${JSON.stringify(event, 2)}`);

  const name = !event.arguments?.name ? "world" : event.arguments.name;

  switch (event.field) {
    case "sayHello":
      return `Hello, ${name}`;
    case "sayGoodbye":
      return `Bye, ${name}`;
    default:
      throw new Error("Unknown field, unable to resolve " + event.field);
  }
};
