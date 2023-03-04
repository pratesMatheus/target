const reverseStr = (txt) => {
  let newStr = "";

  for (let i = txt.length - 1; i >= 0; i--) {
      newStr += txt[i];
  }

  return newStr;
}

reverseStr('hello world');//'dlrow olleh'
reverseStr('matheus'); //'suehtam'
reverseStr('sql'); //'lqs'
reverseStr('target'); //'tegrat'
