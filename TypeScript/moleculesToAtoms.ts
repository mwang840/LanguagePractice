const replacer: (...args: any[]) => string = (_, atom: string, n: number) => atom.repeat(n);
export const parseMolecule = (formula:string): Record<string,number> => formula.replace(/([A-Z][a-z]?)(\d+)/g, replacer)
.replace(/\(((?:[A-Z][a-z]?)+)\)(\d+)/g, replacer)
.replace(/\[((?:[A-Z][a-z]?)+)\](\d+)/g, replacer)
.replace(/\{((?:[A-Z][a-z]?)+)\}(\d+)/g, replacer)
.replace(/[()[\]{}]/g, '')
.replace(/([A-Z][a-z]?)/g, match => `${match} `)
.trim()
.split(' ')
.reduce((acc, v) => ((acc[v] = (acc[v] || 0) + 1), acc), {} as Record<string, number>);