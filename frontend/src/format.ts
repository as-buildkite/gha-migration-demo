/**
 * Small pure utilities used by the frontend to render API responses.
 * Kept dependency-free so the jest tests stay fast.
 */

export function formatGreeting(name: string): string {
  const trimmed = name.trim();
  if (!trimmed) {
    throw new Error("name must not be empty");
  }
  return `Hello, ${trimmed}!`;
}

export function formatTotal(numbers: number[]): string {
  if (numbers.length === 0) {
    throw new Error("numbers must not be empty");
  }
  const total = numbers.reduce((acc, n) => acc + n, 0);
  return `Total: ${total.toLocaleString("en-US")}`;
}

export function slugify(input: string): string {
  return input
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}
