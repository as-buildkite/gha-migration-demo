import { formatGreeting, formatTotal, slugify } from "./format";

describe("formatGreeting", () => {
  it("greets a trimmed name", () => {
    expect(formatGreeting("  Ada ")).toBe("Hello, Ada!");
  });

  it("throws on a blank name", () => {
    expect(() => formatGreeting("   ")).toThrow("name must not be empty");
  });
});

describe("formatTotal", () => {
  it("sums and formats numbers", () => {
    expect(formatTotal([1000, 234])).toBe("Total: 1,234");
  });

  it("throws on empty input", () => {
    expect(() => formatTotal([])).toThrow("numbers must not be empty");
  });
});

describe("slugify", () => {
  it("slugifies a string", () => {
    expect(slugify("Hello, World!")).toBe("hello-world");
  });
});
