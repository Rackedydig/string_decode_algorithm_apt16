# string_decode_algorithm_apt16
## Python script that decodes the strings from APT 16 malware samples; It was made to complement our detailed analysis of the ELMER Backdoor, found on our [blog]()

This script was made to automate the decoding of strings used in APT 16 malware samples. This provides an alternative to dynamic analysis in extracting imteresting strings used by the sample.

The strings used in this example as a Proof of concept come from the binary with hash value 44DD6A777F50E22EC295FEAE2DDEFFFF1849F8307F50DA4435584200A2BA6AF0 (SHA-256), which is the decrypted version of the ELMER backdoor (BED00A7B59EF2BD703098DA6D523A498C8FDA05DCE931F028E8F16FF434DC89E), used by APT16. [VirusTotal link to the sample](https://www.virustotal.com/gui/file/bed00a7b59ef2bd703098da6d523a498c8fda05dce931f028e8f16ff434dc89e/detection)

The malware uses a custom algorithm to encrypt the strings, that can be described shortly: 

### If m is the encrypted buffer and key is the decryption key, the result of the algorithm is (m[i] AND 0xF) XOR (key[i] AND 0xF) + (m[i] AND 0xF0)

## USAGE

### python decode_strings.py strings.txt 

where 'strings.txt' is any text file including strings encrypted with the algorithm described below.

The scripts also uses a wordlist (wordlist.txt) that needs to be in the same folder, in an attempt to filter the output and show only the relevant strings. Only the decoded strings that have a partial match with one of the elements in the wordlist will be displayed in the output, so the quality of the wordlist is important.

## You can read more about the encryption algorithm and the ELMER backdoor, as well as other APT samples and cool tools on our blog, [CyberGeeks](https://cybergeeks.tech/)
