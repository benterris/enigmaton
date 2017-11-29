# Enigmaton

This is a Python encryption algorithm, loosely based on the [Enigma machine](https://en.wikipedia.org/wiki/Enigma_machine) I made in my spare time.  

## Usage

### Simple direct CLI usage

To encrypt, you can simply run :
```bash
python run.py c "super secret key" "Hello world !"
# output : Pa!D;VKqDqS1q
```
And to decrypt :
```bash
python run.py d "super secret key" "Pa!D;VKqDqS1q"
# output : Hello world !
```

### File usage

Alternatively, you can put the text to encrypt or decrypt in the file `input.txt`. If you run the same previous command but without specifying any message to encrypt, then the message will be encrypted/decrypted from `input.txt` to `output.txt`.

To encrypt :
```bash
python run.py c "super secret key"
# output : Message crypted in output file
```
And to decrypt :
```bash
python run.py d "super secret key"
# output : Message decrypted in output file
```

### Rotors setting

Chosing a key only sets the initial position of the rotors. You may want to create your own rotors, which are simply a list of permutations of your alphabet. You can use the function creaRotors which creates random rotors of the correct dimensions (alternatively, you can generate them as you wish). You then have to copy and paste them in the `rotors.txt` file.

## Why another enigma ?

Despite these techniques being very [outdated](https://en.wikipedia.org/wiki/Cryptanalysis_of_the_Enigma), this one has small improvements : the main weakness of the Enigma was encryption and decryption were the exact same process, which implied a letter could *never remain the same* after encryption. The other great weakness was it was difficult to add many physical rotors, so there were usually like 3 of them, and so with big messages you could get a lot of information on the keys.  

Here I got rid of these issues by removing the reflector - the operation that makes encryption the *same* process as decryption - and instead making decryption the *reverse* process, and by adding as many rotors as necessary.
